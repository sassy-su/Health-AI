import React from 'react';

const TeamSection = () => {
  const teamMembers = [
    {
      name: 'Shashank',
      description: 'Student of MVJ College of Engineering, passionate about AI and technology.',
      image: 'https://via.placeholder.com/150',
    },
    {
      name: 'Ragini Kumari', 
      description: 'Student of MVJ College of Engeineering,React frontend developer',
      image: 'https://via.placeholder.com/150',
    },
    {
      name: 'R Sudesh',
      description: 'Student of MVJ Collgege of Engineering',
      image: 'https://via.placeholder.com/150',
    },
  ];

  return (
    <div className="bg-amber-300 py-16 px-8">
      <div className="container mx-auto text-center">
        <h2 className="text-4xl font-bold text-indigo-900 mb-12">Our Team</h2>
        <div className="flex flex-wrap justify-center gap-8">
          {teamMembers.map((member, index) => (
            <div
              key={index}
              className="bg-white rounded-lg shadow-md p-6 w-80 transform hover:scale-105 transition duration-300 ease-in-out"
            >
              <img
                src={member.image}
                alt={member.name}
                className="w-32 h-32 rounded-full mx-auto mb-4"
              />
              <h3 className="text-2xl font-semibold text-indigo-800 mb-2">
                {member.name}
              </h3>
              <p className="text-gray-600">{member.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TeamSection;
