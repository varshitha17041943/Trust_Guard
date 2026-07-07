import React from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { FileText, Download } from 'lucide-react';

export const Reports = () => {
  const reports = [
    { id: 1, name: 'Q3 Security Summary', date: 'Oct 1, 2026', size: '2.4 MB' },
    { id: 2, name: 'Threat Analysis: bank-update.com', date: 'Sep 28, 2026', size: '1.1 MB' }
  ];

  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold flex items-center gap-2"><FileText/> Report Center</h1>
      </div>
      <div className="grid gap-4">
        {reports.map(r => (
          <Card key={r.id} className="p-6 flex items-center justify-between hover:border-primary/50 transition-colors">
            <div className="flex items-center gap-4">
              <div className="bg-white/10 p-3 rounded-lg"><FileText className="w-6 h-6 text-primary" /></div>
              <div>
                <h4 className="font-bold">{r.name}</h4>
                <p className="text-sm text-text-muted">{r.date} • {r.size}</p>
              </div>
            </div>
            <Button variant="outline"><Download className="w-4 h-4 mr-2" /> Download PDF</Button>
          </Card>
        ))}
      </div>
    </div>
  );
};
