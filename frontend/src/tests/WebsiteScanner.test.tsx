import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import WebsiteScanner from '../pages/WebsiteScanner';
import { BrowserRouter } from 'react-router-dom';
import { vi } from 'vitest';

// Mock Framer Motion to avoid animation issues in jsdom
vi.mock('framer-motion', () => ({
  motion: {
    div: ({ children, ...props }: any) => <div {...props}>{children}</div>,
  },
}));

describe('WebsiteScanner Component', () => {
  it('renders correctly', () => {
    render(<BrowserRouter><WebsiteScanner /></BrowserRouter>);
    expect(screen.getByText('Website Scanner')).toBeInTheDocument();
  });

  it('allows typing a URL', () => {
    render(<BrowserRouter><WebsiteScanner /></BrowserRouter>);
    const input = screen.getByPlaceholderText('https://example.com');
    fireEvent.change(input, { target: { value: 'https://test.com' } });
    expect(input).toHaveValue('https://test.com');
  });
});
