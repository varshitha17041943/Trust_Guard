import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const DashboardLayout = () => {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-200 flex">
      <aside className="w-64 bg-slate-800 border-r border-slate-700 hidden md:flex flex-col">
        <div className="h-16 flex items-center px-6 border-b border-slate-700">
          <h1 className="text-xl font-bold text-sky-400">TrustGuardAI</h1>
        </div>
        <nav className="flex-1 px-4 py-6 space-y-2">
          <Link to="/" className="block px-4 py-2 rounded-md hover:bg-slate-700 transition">Dashboard</Link>
          <Link to="/scan" className="block px-4 py-2 rounded-md bg-sky-500/10 text-sky-400 font-medium hover:bg-sky-500/20 transition">New Scan</Link>
        </nav>
      </aside>
      <main className="flex-1 flex flex-col">
        <header className="h-16 border-b border-slate-700 flex items-center justify-between px-6 bg-slate-800/50 backdrop-blur">
          <h2 className="font-semibold">Workspace</h2>
          <div className="w-8 h-8 rounded-full bg-sky-500 flex items-center justify-center font-bold">
            U
          </div>
        </header>
        <div className="p-8 flex-1 overflow-auto">
          <Outlet />
        </div>
      </main>
    </div>
  );
};

export default DashboardLayout;
