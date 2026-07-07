import React from 'react';
import { Card } from '../../components/ui/Card';
import { Bell, ShieldAlert, CheckCircle } from 'lucide-react';

export const Notifications = () => {
  const notifs = [
    { id: 1, title: 'Critical Threat Detected', message: 'A recent scan of bank-update.com returned a Critical risk score of 98.', type: 'danger', time: '2 hours ago' },
    { id: 2, title: 'Weekly Report Ready', message: 'Your weekly security analytics report is ready to download.', type: 'info', time: '1 day ago' },
    { id: 3, title: 'Safe Scan', message: 'google.com was verified as Safe.', type: 'success', time: '2 days ago' }
  ];

  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold flex items-center gap-2"><Bell/> Notifications</h1>
      <Card className="divide-y divide-white/5">
        {notifs.map(n => (
          <div key={n.id} className="p-6 flex gap-4 hover:bg-white/5 transition-colors">
            <div className={`mt-1 rounded-full p-2 ${n.type === 'danger' ? 'bg-danger/20 text-danger' : n.type === 'success' ? 'bg-secondary/20 text-secondary' : 'bg-primary/20 text-primary'}`}>
              {n.type === 'danger' ? <ShieldAlert className="w-5 h-5"/> : <CheckCircle className="w-5 h-5"/>}
            </div>
            <div>
              <h4 className="font-semibold">{n.title}</h4>
              <p className="text-sm text-text-muted mt-1">{n.message}</p>
              <p className="text-xs text-text-muted mt-3 font-medium">{n.time}</p>
            </div>
          </div>
        ))}
      </Card>
    </div>
  );
};
