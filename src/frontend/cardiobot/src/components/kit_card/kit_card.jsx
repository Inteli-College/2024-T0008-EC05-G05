import React, { useEffect, useState } from 'react';
import "./kit_card.css"
import axios from 'axios';

const KitCard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/get-kits');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  // const rows = data.map(item => (
  //   JSON.stringify(item)
  // ))

  return ( 
    <section className='kit-card area'>
      <h1>Data from Flask Backend</h1>
        {Array.isArray(data) ? (
          data.map(item => (
            <div className='kit-card item'>
              <p key={item.id}>{item.kit_name}</p>
            </div>
          ))
        ) : (
          <p>Data is not an array.</p>
        )}
    </section>
  );
};

export default KitCard;
