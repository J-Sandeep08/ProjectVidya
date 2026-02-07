import React from 'react';

interface Props {
  navigateTo: (page: any) => void;
  updateAppState: (data: any) => void;
}

const LoginPage: React.FC<Props> = ({ navigateTo, updateAppState }) => {
  const handleLogin = () => {
    updateAppState({
      currentUser: {
        firstName: 'Demo',
        lastName: 'User',
        email: 'demo@gmail.com',
        username: 'demo_user',
      },
    });
    navigateTo('dashboard');
  };

  return (
    <div className="flex min-h-screen items-center justify-center">
      <button
        onClick={handleLogin}
        className="px-6 py-3 bg-blue-600 text-white rounded"
      >
        Login
      </button>
    </div>
  );
};

export default LoginPage;
