import React, { useEffect, useState } from 'react';
import axios from 'axios';
import "./positions_catcher.css"

const DataComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/get-positions');
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
    <div>
      <h1>Data from Flask Backend</h1>
      <section className='positions-area'>
        {Array.isArray(data) ? (
          data.map(item => (
            <div className='position-card'>
              <p key={item.id}>{item.position_name}</p>
            </div>
          ))
        ) : (
          <p>Data is not an array.</p>
        )}
      </section>
    </div>
  );
};

export default DataComponent;
