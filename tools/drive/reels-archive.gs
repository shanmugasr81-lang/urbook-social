/**
 * urbook – Reels archive + 7-day clean-up (Google Apps Script, owner contact@urbook.co.uk)
 * Shan, 25 Nov 2026: "Once it is read move to archive folder. So house keep can delete it after 7 days."
 *
 * Why a script: the Claude / agent Drive connection may only move or delete files IT created, so it
 * cannot move videos Shan uploads. Agents add a row to the 'Reels read log' sheet when they have read
 * a reel; this script (running as Shan) does the moving and the clean-up once a day.
 *
 * Setup (once, 2 minutes): open https://script.google.com → New project → paste this file →
 * Run 'setup' → allow access (your own account) → done. It then runs every night at ~02:00 UK.
 */
const REELS_FOLDER = '1AyJBa7fjryix0ZkSSPkP-4cQoiFuPHlY';
const ARCHIVE_FOLDER = '1Z8BeKT8G2Y9C7tCllGMZos0eGfypO_Zl';
const READ_LOG = '12aAGNcG0GOrrd24xPjqJo-MwjuFTzpPM5WIuDOJKePE';
const KEEP_DAYS = 7;

function setup() {
  ScriptApp.getProjectTriggers().forEach((t) => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('nightly').timeBased().atHour(2).everyDays(1).inTimezone('Europe/London').create();
  nightly();
}

function nightly() {
  const archive = DriveApp.getFolderById(ARCHIVE_FOLDER);
  const rows = SpreadsheetApp.openById(READ_LOG).getSheets()[0].getDataRange().getValues();
  const col = rows[0].indexOf('fileId');
  const movedCol = rows[0].indexOf('archivedAt');
  const sheet = SpreadsheetApp.openById(READ_LOG).getSheets()[0];
  const outCol = movedCol >= 0 ? movedCol : rows[0].length;
  if (movedCol < 0) sheet.getRange(1, outCol + 1).setValue('archivedAt');
  // 1) Move every logged, not yet archived reel into Archive (never the folders or the log itself).
  for (let i = 1; i < rows.length; i++) {
    const id = String(rows[i][col] || '').trim();
    if (!id || (movedCol >= 0 && rows[i][movedCol])) continue;
    try {
      const f = DriveApp.getFileById(id);
      if (f.getId() === READ_LOG) continue;
      f.moveTo(archive);
      f.setDescription('Archived ' + new Date().toISOString() + ' – read by urbook agents');
      sheet.getRange(i + 1, outCol + 1).setValue(new Date().toISOString());
    } catch (e) { sheet.getRange(i + 1, outCol + 1).setValue('error: ' + e.message); }
  }
  // 2) Archive files older than KEEP_DAYS (counted from when they were archived) go to the Drive bin
  //    (Google keeps the bin 30 days, so a mistake can still be undone).
  const cutoff = Date.now() - KEEP_DAYS * 864e5;
  const it = archive.getFiles();
  while (it.hasNext()) {
    const f = it.next();
    const m = /Archived (\S+)/.exec(f.getDescription() || '');
    const at = m ? Date.parse(m[1]) : f.getLastUpdated().getTime();
    if (at < cutoff) f.setTrashed(true);
  }
}
