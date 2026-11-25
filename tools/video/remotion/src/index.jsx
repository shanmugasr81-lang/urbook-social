// urbook StoryReel – 1080x1920 story reel driven by a props JSON (scenes of real clips/photos + captions).
// Render: npx remotion render src/index.jsx StoryReel out.mp4 --props=reel.json --browser-executable="$URBOOK_CHROME"
import {registerRoot, Composition, AbsoluteFill, Sequence, OffthreadVideo, Img, Audio, staticFile, useCurrentFrame, interpolate} from 'remotion';
import React from 'react';
const INK = '#0E2A47', SUN = '#F5821F';
const SAFE = {top: 230, bottom: 480, right: 230, left: 60}; // Instagram/TikTok safe zone on 1080x1920
const Media = ({src, start = 0}) => !src ? <AbsoluteFill style={{background: INK}}/> :
  /\.(mp4|mov|webm)$/i.test(src) ? <OffthreadVideo startFrom={Math.round(start * 30)} src={src.startsWith("http") ? src : staticFile(src)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}}/> :
  <Img src={src.startsWith('http') ? src : staticFile(src)} style={{width: '100%', height: '100%', objectFit: 'cover'}}/>;
const Text = ({text, big}) => { const f = useCurrentFrame(); const o = interpolate(f, [0, 6], [0, 1], {extrapolateRight: 'clamp'});
  return <div style={{position: 'absolute', left: SAFE.left, right: SAFE.right, top: big ? SAFE.top + 120 : undefined, bottom: big ? undefined : SAFE.bottom,
    opacity: o, color: '#fff', fontFamily: 'sans-serif', fontWeight: 800, fontSize: big ? 96 : 60, lineHeight: 1.1,
    textShadow: '0 4px 18px rgba(0,0,0,.65)'}}>{big ? <span style={{background: SUN, padding: '6px 18px', borderRadius: 14}}>{text}</span> : text}</div>; };
const StoryReel = ({scenes = [], music, fps = 30}) => { let at = 0;
  return <AbsoluteFill style={{background: INK}}>
    {scenes.map((s, i) => { const d = Math.round((s.seconds || 2.5) * fps); const el =
      <Sequence key={i} from={at} durationInFrames={d}><Media src={s.src} start={s.start}/><AbsoluteFill style={{background: 'linear-gradient(transparent 55%, rgba(0,0,0,.55))'}}/>
        {s.hook && <Text text={s.hook} big/>}{s.caption && <Text text={s.caption}/>}</Sequence>; at += d; return el; })}
    {music && <Audio src={staticFile(music)} volume={0.35}/>}
  </AbsoluteFill>; };
const len = p => Math.max(30, Math.round((p.scenes || []).reduce((a, s) => a + (s.seconds || 2.5), 0) * 30));
registerRoot(() => <Composition id="StoryReel" component={StoryReel} fps={30} width={1080} height={1920}
  durationInFrames={300} defaultProps={{scenes: []}} calculateMetadata={({props}) => ({durationInFrames: len(props)})}/>);
