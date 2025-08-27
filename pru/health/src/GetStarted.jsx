import React, { useState } from 'react';

const GetStarted = () => {
  const [gender, setGender] = useState('');

  const handleGenderChange = (value) => {
    setGender(value);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-8">
      <h1 className="text-4xl font-bold mb-8">Get Started with Your Health</h1>
      <form className="bg-white p-8 rounded-lg shadow-lg w-full max-w-lg">
        <div className="mb-6">
          <label className="block text-xl font-semibold mb-2">Name:</label>
          <input type="text" className="border p-3 w-full text-lg" />
        </div>
        <div className="mb-6">
          <label className="block text-xl font-semibold mb-2">Age:</label>
          <input type="number" className="border p-3 w-full text-lg" />
        </div>
        <div className="mb-6">
          <label className="block text-xl font-semibold mb-2">Gender:</label>
          <div className="flex justify-between">
            <div 
              className={`flex flex-col items-center cursor-pointer ${gender === 'male' ? 'border-2 border-blue-500' : ''}`} 
              onClick={() => handleGenderChange('male')}
            >
              <img 
                src="https://via.placeholder.com/100" 
                alt="Male" 
                className="w-24 h-24 mb-2 rounded-full"
              />
              <span className="text-lg">Male</span>
            </div>
            <div 
              className={`flex flex-col items-center cursor-pointer ${gender === 'female' ? 'border-2 border-pink-500' : ''}`} 
              onClick={() => handleGenderChange('female')}
            >
              <img 
                src="https://via.placeholder.com/100" 
                alt="Female" 
                className="w-24 h-24 mb-2 rounded-full"
              />
              <span className="text-lg">Female</span>
            </div>
          </div>
        </div>
        {/* Add more inputs as needed */}
        <button type="submit" className="bg-blue-500 text-white py-3 px-6 rounded-lg text-lg">Submit</button>
      </form>
    </div>
  );
};

export default GetStarted;
