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
    <section className='kit-card-area'>
        {Array.isArray(data) ? (
          data.map(item => (
            <div className='kit-card-item' key={item.id}>
              <h3 className='kit-card-title'>{item.kit_name}</h3>
              <p className='kit-car-dec'>{item.kit_desc}</p>
              <div className='kit-carad-img-area'>
                <img src={item.kit_img} alt="" className='kit-card-img'/>
              </div>
              <div className='kit-card-buttons-area'>
                <button type="button">Edit</button>
                <button type="button">Start</button>
              </div>
            </div>
          ))
        ) : (
          <p>Data is not an array.</p>
        )}
    </section>
  );
};

export default KitCard;
