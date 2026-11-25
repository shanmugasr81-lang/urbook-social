// urbook StoryReel v2 – 1080x1920 story reel driven by a props JSON.
// v2 (25 Nov 2026): per-scene voiceover (voice), music ducked under voice, urbook logo, offer chip + end card.
// Build props + voice with tools/video/make_reel.py, then:
// npx remotion render src/index.jsx StoryReel out.mp4 --props=reel.json --browser-executable="$URBOOK_CHROME"
import {registerRoot, Composition, AbsoluteFill, Sequence, OffthreadVideo, Img, Audio, staticFile, useCurrentFrame, interpolate} from 'remotion';
import React from 'react';
const INK = '#0E2A47', SUN = '#F5821F';
const SAFE = {top: 230, bottom: 480, right: 230, left: 60}; // Instagram/TikTok safe zone on 1080x1920
const FPS = 30, END_S = 3;
const url = s => (s.startsWith('http') ? s : staticFile(s));
const Media = ({src, start = 0, sound = false}) => !src ? <AbsoluteFill style={{background: INK}}/> :
  /\.(mp4|mov|webm)$/i.test(src) ? <OffthreadVideo startFrom={Math.round(start * FPS)} src={url(src)} muted={!sound} volume={1} style={{width: '100%', height: '100%', objectFit: 'cover'}}/> :
  <Img src={url(src)} style={{width: '100%', height: '100%', objectFit: 'cover'}}/>;
const fade = () => interpolate(useCurrentFrame(), [0, 6], [0, 1], {extrapolateRight: 'clamp'});
const Text = ({text, big}) => <div style={{position: 'absolute', left: SAFE.left, right: SAFE.right, top: big ? SAFE.top + 130 : undefined, bottom: big ? undefined : SAFE.bottom,
    opacity: fade(), color: '#fff', fontFamily: 'sans-serif', fontWeight: 800, fontSize: big ? 92 : 58, lineHeight: 1.12,
    textShadow: '0 4px 18px rgba(0,0,0,.7)'}}>{big ? <span style={{background: SUN, padding: '6px 18px', borderRadius: 14, boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone'}}>{text}</span> : text}</div>;
const Logo = ({logo, size = 96, style}) => logo ? <div style={{background: 'rgba(255,255,255,.94)', borderRadius: size * .22, padding: `${size * .12}px ${size * .22}px`, display: 'inline-flex', ...style}}><Img src={url(logo)} style={{height: size}}/></div> : null;
const Chip = ({offer}) => offer ? <div style={{position: 'absolute', left: SAFE.left, bottom: SAFE.bottom - 110, background: SUN, color: '#fff',
    fontFamily: 'sans-serif', fontWeight: 800, fontSize: 40, padding: '10px 22px', borderRadius: 40, opacity: fade()}}>{offer.chip}</div> : null;
const EndCard = ({end = {}, offer, logo, src, start}) => <AbsoluteFill>
  <Media src={src} start={start}/><AbsoluteFill style={{background: 'rgba(14,42,71,.82)'}}/>
  <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: `${SAFE.top}px ${SAFE.right}px ${SAFE.bottom}px ${SAFE.left}px`, opacity: fade(),
    color: '#fff', fontFamily: 'sans-serif', textAlign: 'center', gap: 34}}>
    <Logo logo={logo} size={190}/>
    {end.title && <div style={{fontSize: 66, fontWeight: 800, lineHeight: 1.1}}>{end.title}</div>}
    {end.line && <div style={{fontSize: 46, fontWeight: 600, opacity: .92}}>{end.line}</div>}
    {offer && <div style={{background: SUN, fontSize: 44, fontWeight: 800, padding: '14px 28px', borderRadius: 18}}>{offer.end}</div>}
    <div style={{fontSize: 52, fontWeight: 800, borderBottom: `6px solid ${SUN}`, paddingBottom: 6}}>{end.cta || 'Book at urbooktravel.com'}</div>
  </AbsoluteFill></AbsoluteFill>;
// keepSound (25 Nov 2026, Shan): the clip's own voice + music are kept exactly; no music bed, no AI voice.
const StoryReel = ({scenes = [], music, logo, offer, end, chipFrom, keepSound = false}) => { let at = 0; const hasVoice = scenes.some(s => s.voice);
  const items = scenes.map((s, i) => { const d = Math.round((s.seconds || 2.5) * FPS); const el =
    <Sequence key={i} from={at} durationInFrames={d}><Media src={s.src} start={s.start} sound={keepSound}/><AbsoluteFill style={{background: 'linear-gradient(transparent 50%, rgba(0,0,0,.6))'}}/>
      {s.hook && <Text text={s.hook} big/>}{(s.caption || s.say) && <Text text={s.caption || s.say}/>}
      <Logo logo={logo} size={78} style={{position: 'absolute', top: SAFE.top + 10, right: SAFE.right - 170}}/>
      {s.voice && <Audio src={url(s.voice)} volume={1}/>}
      {offer && i >= (chipFrom ?? scenes.length - 2) && <Chip offer={offer}/>}</Sequence>; at += d; return el; });
  const last = scenes[scenes.length - 1] || {};
  return <AbsoluteFill style={{background: INK}}>
    {items}
    {end !== false && <Sequence from={at} durationInFrames={END_S * FPS}><EndCard end={end} offer={offer} logo={logo} src={last.src} start={(last.start || 0) + (last.seconds || 0)}/></Sequence>}
    {music && !keepSound && <Audio src={url(music)} volume={hasVoice ? 0.12 : 0.35}/>}
  </AbsoluteFill>; };
const len = p => Math.max(30, Math.round(((p.scenes || []).reduce((a, s) => a + (s.seconds || 2.5), 0) + (p.end === false ? 0 : END_S)) * FPS));
registerRoot(() => <Composition id="StoryReel" component={StoryReel} fps={FPS} width={1080} height={1920}
  durationInFrames={300} defaultProps={{scenes: []}} calculateMetadata={({props}) => ({durationInFrames: len(props)})}/>);
