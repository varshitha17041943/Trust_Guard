import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { RiskBadge } from '../../components/ui/RiskBadge';
import { Search, Filter, Download, Trash2, Eye } from 'lucide-react';
import { Link } from 'react-router-dom';

const mockHistory = [
  { id: 1, url: 'secure-login.bank-update.com', risk: 'High', score: 85, date: '2026-07-06 14:30', status: 'Blocked' },
  { id: 2, url: 'github.com', risk: 'Safe', score: 5, date: '2026-07-06 12:15', status: 'Safe' }
];

export const History = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const filtered = mockHistory.filter(h => h.url.includes(searchTerm));

  return (
    <div className='space-y-8'>
      <h1 className='text-2xl font-bold'>Scan History</h1>
      <Card className='p-0 overflow-hidden'>
        <div className='overflow-x-auto'>
          <table className='w-full text-sm text-left'>
            <thead className='text-text-muted bg-white/5 uppercase text-xs tracking-wider'>
              <tr>
                <th className='px-6 py-4 font-medium'>Website</th>
                <th className='px-6 py-4 font-medium'>Risk Level</th>
                <th className='px-6 py-4 font-medium'>Score</th>
                <th className='px-6 py-4 font-medium text-right'>Action</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((scan) => (
                <tr key={scan.id} className='border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors'>
                  <td className='px-6 py-4 font-medium'>{scan.url}</td>
                  <td className='px-6 py-4'><RiskBadge level={scan.risk as any} /></td>
                  <td className='px-6 py-4'>{scan.score}/100</td>
                  <td className='px-6 py-4 text-right flex justify-end gap-2'>
                    <Link to={`/app/results/${scan.id}`}>
                      <Button variant='ghost' size='sm'><Eye className='w-4 h-4' /></Button>
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
};
