import React from 'react';

const HomeBody = () => {
  return (
    <div
      id="content-section"
      className="bg-gradient-to-b from-gray-800 to-gray-900 text-white min-h-screen flex items-center justify-center p-8"
    >
      <div className="container mx-auto flex flex-col md:flex-row items-center justify-center space-y-10 md:space-y-0 md:space-x-10">
        {/* Left Half: Quote */}
        <div className="md:w-1/2 text-center md:text-left">
          <h1 className="text-5xl font-bold text-indigo-300 mb-6 animate-fade-in-down">
            "The greatest wealth is health."
          </h1>
          <p className="text-2xl text-gray-300 leading-relaxed animate-fade-in-up">
            Taking care of your body is essential. Health is not just about what you’re eating. It’s also about what you’re thinking and saying.
            <br /><br />
            A healthy outside starts from the inside. Remember to nurture both your body and your mind for a truly holistic well-being.
          </p>
        </div>

        {/* Right Half: Image */}
        <div className="md:w-1/2 animate-slide-in-right">
          <img
            src="https://tandempsychology.com/wp-content/uploads/2023/04/chart.png"
            alt="Health and Wellness"
            className="w-3/4 h-auto rounded-2xl shadow-2xl"
          />
        </div>
      </div>
    </div>
  );
};

export default HomeBody;
