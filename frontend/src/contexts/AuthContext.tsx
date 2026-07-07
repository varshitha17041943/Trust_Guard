import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../utils/axios';

type User = { id: number; email: string; role: string };
type AuthContextType = { user: User | null; loading: boolean; login: (token: string, u: User) => void; logout: () => void; };

const AuthContext = createContext<AuthContextType>({ user: null, loading: true, login: () => {}, logout: () => {} });

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem('access_token');
      if (token) {
        try {
          const res = await api.get('/auth/profile');
          setUser(res.data);
        } catch {
          localStorage.removeItem('access_token');
        }
      }
      setLoading(false);
    };
    checkAuth();
  }, []);

  const login = (token: string, u: User) => {
    localStorage.setItem('access_token', token);
    setUser(u);
  };

  const logout = async () => {
    try {
      await api.post('/auth/logout');
    } catch (e) { console.error(e) }
    localStorage.removeItem('access_token');
    setUser(null);
    window.location.href = '/login';
  };

  return <AuthContext.Provider value={{ user, loading, login, logout }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);
