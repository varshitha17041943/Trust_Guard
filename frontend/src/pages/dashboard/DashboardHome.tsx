import React from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { Shield, AlertTriangle, CheckCircle, Search, QrCode, FileText, Activity } from 'lucide-react';

const recentScans = [
  { id: 1, url: 'secure-login.bank-update.com', risk: 'High', date: '2026-07-06 14:30', status: 'Blocked' },
  { id: 2, url: 'github.com', risk: 'Low', date: '2026-07-06 12:15', status: 'Safe' },
  { id: 3, url: 'paypal-verify-account.net', risk: 'Critical', date: '2026-07-06 09:45', status: 'Blocked' },
  { id: 4, url: 'cloudflare.com', risk: 'Low', date: '2026-07-05 18:20', status: 'Safe' },
];

export const DashboardHome = () => {
  return (
    <div className='space-y-8'>
      <div className='flex justify-between items-end'>
        <div>
          <h1 className='text-2xl font-bold'>Dashboard Overview</h1>
          <p className='text-text-muted mt-1'>Welcome back, here is your security summary.</p>
        </div>
        <Button>Generate Report</Button>
      </div>

      {/* Stats Grid */}
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6'>
        <Card className='bg-gradient-to-br from-primary/20 to-background'>
          <div className='flex items-center justify-between mb-4'>
            <h3 className='text-sm font-medium text-text-muted'>Today's Scans</h3>
            <Activity className='h-5 w-5 text-primary' />
          </div>
          <div className='text-3xl font-bold'>124</div>
          <p className='text-sm text-secondary mt-2'>+14% from yesterday</p>
        </Card>
        <Card>
          <div className='flex items-center justify-between mb-4'>
            <h3 className='text-sm font-medium text-text-muted'>Safe Websites</h3>
            <CheckCircle className='h-5 w-5 text-secondary' />
          </div>
          <div className='text-3xl font-bold'>112</div>
        </Card>
        <Card>
          <div className='flex items-center justify-between mb-4'>
            <h3 className='text-sm font-medium text-text-muted'>Dangerous Websites</h3>
            <AlertTriangle className='h-5 w-5 text-danger' />
          </div>
          <div className='text-3xl font-bold'>12</div>
        </Card>
        <Card>
          <div className='flex items-center justify-between mb-4'>
            <h3 className='text-sm font-medium text-text-muted'>Average Risk</h3>
            <Shield className='h-5 w-5 text-warning' />
          </div>
          <div className='text-3xl font-bold'>24/100</div>
        </Card>
      </div>

      {/* Quick Actions & Tip */}
      <div className='grid grid-cols-1 lg:grid-cols-3 gap-6'>
        <Card className='lg:col-span-2'>
          <h3 className='font-semibold mb-4'>Quick Actions</h3>
          <div className='grid sm:grid-cols-2 gap-4'>
            <Button variant='outline' className='h-auto py-4 flex flex-col items-center justify-center gap-2'>
              <Search className='h-6 w-6' />
              <span>Scan Website</span>
            </Button>
            <Button variant='outline' className='h-auto py-4 flex flex-col items-center justify-center gap-2'>
              <QrCode className='h-6 w-6' />
              <span>Scan QR Code</span>
            </Button>
          </div>
        </Card>
        <Card className='bg-secondary/10 border-secondary/20 flex flex-col justify-center'>
          <div className='flex items-center gap-2 mb-3'>
            <Shield className='h-5 w-5 text-secondary' />
            <h3 className='font-semibold text-secondary'>Cyber Safety Tip</h3>
          </div>
          <p className='text-sm text-text-muted'>
            Never share OTPs. Always check URLs carefully before entering login credentials, especially if you clicked a link in an email or SMS.
          </p>
        </Card>
      </div>

      {/* Recent Scans Table */}
      <Card>
        <div className='flex items-center justify-between mb-6'>
          <h3 className='font-semibold'>Recent Scans</h3>
          <Button variant='ghost' size='sm'>View All</Button>
        </div>
        <div className='overflow-x-auto'>
          <table className='w-full text-sm text-left'>
            <thead className='text-text-muted bg-white/5'>
              <tr>
                <th className='px-4 py-3 rounded-l-lg font-medium'>Website</th>
                <th className='px-4 py-3 font-medium'>Risk Level</th>
                <th className='px-4 py-3 font-medium'>Date</th>
                <th className='px-4 py-3 font-medium'>Status</th>
                <th className='px-4 py-3 rounded-r-lg font-medium'>Action</th>
              </tr>
            </thead>
            <tbody>
              {recentScans.map((scan) => (
                <tr key={scan.id} className='border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors'>
                  <td className='px-4 py-4 font-medium'>{scan.url}</td>
                  <td className='px-4 py-4'>
                    <Badge variant={scan.risk === 'Low' ? 'success' : scan.risk === 'High' ? 'warning' : 'danger'}>
                      {scan.risk}
                    </Badge>
                  </td>
                  <td className='px-4 py-4 text-text-muted'>{scan.date}</td>
                  <td className='px-4 py-4'>
                    <span className={scan.status === 'Safe' ? 'text-secondary' : 'text-danger'}>{scan.status}</span>
                  </td>
                  <td className='px-4 py-4'>
                    <Button variant='ghost' size='sm'>View Details</Button>
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
