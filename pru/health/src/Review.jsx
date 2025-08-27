import React from 'react';

const ReviewSection = () => {
  // Updated review data with six members
  const reviews = [
    {
      name: 'Alice Johnson',
      review: 'Amazing experience! The AI Health Monitor has truly made my life easier.',
      image: 'https://randomuser.me/api/portraits/women/1.jpg',
      rating: 5,
    },
    {
      name: 'Michael Brown',
      review: 'Very intuitive and easy to use. Highly recommend it to everyone.',
      image: 'https://randomuser.me/api/portraits/men/2.jpg',
      rating: 4,
    },
    {
      name: 'Sophia Lee',
      review: 'A fantastic tool for keeping track of my health metrics. Love the insights!',
      image: 'https://randomuser.me/api/portraits/women/3.jpg',
      rating: 5,
    },
    {
      name: 'James Smith',
      review: 'The AI predictions are spot-on. A must-have app for health monitoring.',
      image: 'https://randomuser.me/api/portraits/men/4.jpg',
      rating: 4,
    },
    {
      name: 'Emma Wilson',
      review: 'Very impressed with the accuracy and ease of use. The interface is user-friendly.',
      image: 'https://randomuser.me/api/portraits/women/5.jpg',
      rating: 5,
    },
    {
      name: 'Liam Carter',
      review: 'Excellent tool for health tracking. The insights are very helpful and clear.',
      image: 'https://randomuser.me/api/portraits/men/6.jpg',
      rating: 4,
    },
    {
      name: 'Allen aerza',
      review: 'Amazing experience! The AI Health Monitor has truly made my life easier and good suggestions.',
      image: 'https://randomuser.me/api/portraits/women/6.jpg',
      rating: 5,
    },
    {
      name: 'Alice Johnson',
      review: 'Amazing experience! The AI Health Monitor has truly made my life easier and pretty to access them allover.',
      image: 'https://randomuser.me/api/portraits/men/7.jpg',
      rating: 4,
    },
    {
      name: 'daisy',
      review: 'Better and best everyday.',
      image: 'https://randomuser.me/api/portraits/women/7.jpg',
      rating: 5,
    },
  ];

  // Function to render star ratings
  const renderStars = (rating) => {
    return Array.from({ length: 5 }, (_, index) => (
      <span key={index} className={index < rating ? 'text-yellow-400' : 'text-gray-500'}>
        ★
      </span>
    ));
  };

  return (
    <div className="bg-gray-800 py-16 px-8 text-white">
      <div className="container mx-auto text-center">
        <h2 className="text-4xl font-bold mb-12">User Reviews</h2>
        <div className="flex flex-wrap justify-center gap-8">
          {reviews.map((review, index) => (
            <div
              key={index}
              className="bg-gray-900 rounded-lg shadow-lg p-6 w-80 transform hover:scale-105 transition duration-300 ease-in-out"
            >
              <img
                src={review.image}
                alt={review.name}
                className="w-24 h-24 rounded-full mx-auto mb-4 border-4 border-gray-700"
              />
              <h3 className="text-2xl font-semibold mb-2">{review.name}</h3>
              <div className="flex justify-center mb-4">
                {renderStars(review.rating)}
              </div>
              <p className="text-gray-300">{review.review}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ReviewSection;
