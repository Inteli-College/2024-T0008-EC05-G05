import React, { useEffect, useState } from 'react';
import "./kit_card.css"
import axios from 'axios';
import kitImage from '../../assets/imgs/imagem_kits.png';
import { useNavigate } from "react-router-dom";


const KitCard = () => {
  const [data, setData] = useState([]);
  const change_page = useNavigate();


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/posts/');
        setData(response.data);
        console.log(response.data)
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
              <h3 className='kit-card-title'>{item.nome_kit}</h3>
              {/* Todo adicionar a descrição de cada kit  */}
              {/* <p className='kit-car-dec'>{item.id_kit}</p> */}
              <div className='kit-carad-img-area'>
                <img src={kitImage} alt="" className='kit-card-img'/>
              </div>
              <div className='kit-card-buttons-area'>
                <button type="button" >Edit</button>
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
