import React from 'react';
import { CheckCircle2 } from 'lucide-react';

export const Timeline = () => {
  const events = [
    { time: '09:41:02', label: 'URL structure validated' },
    { time: '09:41:03', label: 'SSL certificate chain verified' },
    { time: '09:41:03', label: 'WHOIS domain registry parsed' },
    { time: '09:41:04', label: 'Threat intelligence cross-reference' },
    { time: '09:41:05', label: 'Risk algorithm complete' }
  ];

  return (
    <div className="space-y-4">
      <h3 className="font-semibold text-sm uppercase tracking-widest text-text-muted mb-4">Execution Timeline</h3>
      <div className="space-y-4 pl-2 border-l border-white/10 ml-2">
        {events.map((ev, i) => (
          <div key={i} className="relative pl-6">
            <div className="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-background border-2 border-primary flex items-center justify-center">
              <div className="w-1.5 h-1.5 bg-primary rounded-full" />
            </div>
            <p className="text-xs text-primary font-mono mb-0.5">{ev.time}</p>
            <p className="text-sm text-text-muted">{ev.label}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
