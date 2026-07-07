import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import { Shield, Menu, X, Moon, Sun } from 'lucide-react';
import { Button } from '../components/ui/Button';
import { cn } from '../utils/cn';

export const RootLayout = () => {
  const [isMenuOpen, setIsMenuOpen] = React.useState(false);
  
  return (
    <div className='min-h-screen flex flex-col'>
      <nav className='sticky top-0 z-50 glass-panel border-b border-white/10'>
        <div className='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8'>
          <div className='flex items-center justify-between h-16'>
            <div className='flex items-center gap-2'>
              <Shield className='h-8 w-8 text-primary' />
              <span className='font-bold text-xl tracking-tight'>TrustGuard<span className='text-primary'>AI</span></span>
            </div>
            <div className='hidden md:flex items-center space-x-8'>
              <Link to='/' className='text-text-muted hover:text-white transition-colors relative group'>
                Home
                <span className='absolute -bottom-1 left-0 w-0 h-0.5 bg-primary transition-all group-hover:w-full'></span>
              </Link>
              <Link to='/dashboard' className='text-text-muted hover:text-white transition-colors relative group'>
                Dashboard
                <span className='absolute -bottom-1 left-0 w-0 h-0.5 bg-primary transition-all group-hover:w-full'></span>
              </Link>
            </div>
            <div className='hidden md:flex items-center space-x-4'>
              <Button variant='ghost' size='sm'>Login</Button>
              <Link to='/dashboard'><Button size='sm'>Get Started</Button></Link>
            </div>
            <div className='md:hidden'>
              <button onClick={() => setIsMenuOpen(!isMenuOpen)} className='text-text-muted'>
                {isMenuOpen ? <X /> : <Menu />}
              </button>
            </div>
          </div>
        </div>
      </nav>
      <main className='flex-1'>
        <Outlet />
      </main>
      <footer className='border-t border-white/10 bg-background-paper/50 py-12 mt-20'>
        <div className='max-w-7xl mx-auto px-4 text-center text-text-muted'>
          <div className='flex justify-center items-center gap-2 mb-4'>
            <Shield className='h-6 w-6 text-primary' />
            <span className='font-bold text-lg text-white'>TrustGuardAI</span>
          </div>
          <p>© 2026 TrustGuardAI. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};
