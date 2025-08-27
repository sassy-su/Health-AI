import React from 'react';

const NavBar = () => {
  const handleGetStarted = () => {
    window.location.href = "http://localhost:8501";
  };

  return (
    <nav className="bg-gray-800 text-white p-4  w-full z-10">
      <div className="flex justify-between">
        <div className="text-lg font-bold">AI Fitness And Mental Health Suggestions</div>
        <div className="space-x-8 text-xl">
          <a href="#home" className="hover:text-yellow-400">Home</a>
          <a href="#about" className="hover:text-yellow-400">About</a>
          <a href="#team" className="hover:text-yellow-400">Team</a>
          <a href="#services" className="hover:text-yellow-400">Services</a>
          <a href="#contact" className="hover:text-yellow-400">Contact</a>
          <button 
            onClick={handleGetStarted} 
            className="bg-yellow-400 text-gray-800 font-bold py-2 px-4 rounded hover:bg-yellow-300 transition duration-300"
          >
            Get Started
          </button>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
