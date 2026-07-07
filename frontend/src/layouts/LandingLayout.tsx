import React from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const LandingLayout = () => {
  return (
    <div className="min-h-screen flex flex-col relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-background via-surface to-background animate-gradient-x -z-10"></div>
      <Navbar />
      <main className="flex-1 flex flex-col pt-20">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default LandingLayout;
