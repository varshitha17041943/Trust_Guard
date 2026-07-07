import React, { useEffect, useState } from 'react';

export const AdminDashboard = () => {
    const [stats, setStats] = useState({total_users: 0, total_scans: 0, blocked_urls: 0, active_threats: 0});
    
    useEffect(() => {
        fetch('/api/admin/stats')
            .then(res => res.json())
            .then(data => setStats(data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div className="min-h-screen bg-black text-white p-8">
            <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Total Users</h3>
                    <p className="text-3xl font-bold text-white mt-2">{stats.total_users}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Total Scans</h3>
                    <p className="text-3xl font-bold text-blue-400 mt-2">{stats.total_scans}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Blocked URLs</h3>
                    <p className="text-3xl font-bold text-red-500 mt-2">{stats.blocked_urls}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Active Threats</h3>
                    <p className="text-3xl font-bold text-orange-400 mt-2">{stats.active_threats}</p>
                </div>
            </div>
        </div>
    );
};
