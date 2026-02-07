import React from 'react';

const EligibilityVerificationPage = ({ navigateTo }: any) => {
  return (
    <div className="p-6">
      <h2 className="text-xl font-bold">Eligibility Verification</h2>
      <button
        onClick={() => navigateTo('dashboard')}
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
      >
        Back to Dashboard
      </button>
    </div>
  );
};

export default EligibilityVerificationPage;
