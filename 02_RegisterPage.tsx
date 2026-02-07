import React from 'react';

const RegisterPage = ({ navigateTo }: any) => {
  return (
    <div className="flex min-h-screen items-center justify-center">
      <button
        onClick={() => navigateTo('login')}
        className="px-6 py-3 bg-green-600 text-white rounded"
      >
        Go to Login
      </button>
    </div>
  );
};

export default RegisterPage;
