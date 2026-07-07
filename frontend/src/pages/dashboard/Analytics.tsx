import React, { useEffect, useState } from 'react';
import { Card } from '../../components/ui/Card';
import { api, ensureAuthenticated } from '../../services/api';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

export const Analytics = () => {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    const load = async () => {
      await ensureAuthenticated();
      try {
        const res = await api.get('/dashboard/stats');
        setStats(res.data);
      } catch (err) {}
    };
    load();
  }, []);

  const pieData = [
    { name: 'Safe', value: stats?.safe_websites || 10, color: '#10B981' },
    { name: 'Dangerous', value: stats?.dangerous_websites || 5, color: '#EF4444' }
  ];

  const barData = [
    { name: 'Mon', scans: 12 }, { name: 'Tue', scans: 19 }, { name: 'Wed', scans: 15 },
    { name: 'Thu', scans: 22 }, { name: 'Fri', scans: 30 }, { name: 'Sat', scans: 8 }, { name: 'Sun', scans: 5 }
  ];

  return (
    <div className="space-y-8 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold">Analytics Dashboard</h1>
      <div className="grid md:grid-cols-2 gap-6">
        <Card className="p-6">
          <h3 className="font-semibold mb-4">Risk Distribution</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={pieData} innerRadius={60} outerRadius={80} paddingAngle={5} dataKey="value">
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </Card>
        <Card className="p-6">
          <h3 className="font-semibold mb-4">Weekly Scan Volume</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData}>
                <XAxis dataKey="name" stroke="#666" />
                <YAxis stroke="#666" />
                <Tooltip cursor={{fill: 'rgba(255,255,255,0.05)'}} contentStyle={{backgroundColor: '#1a1a1a', border: 'none', borderRadius: '8px'}} />
                <Bar dataKey="scans" fill="#3B82F6" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </Card>
      </div>
    </div>
  );
};
