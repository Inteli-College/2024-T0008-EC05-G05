import React, { useEffect, useState } from 'react';
import "./kit_card.css"
import axios from 'axios';
import kitImage from '../../assets/imgs/imagem_kits.png';
import { useNavigate } from "react-router-dom";
import Modal from '../kit_description_popup/KitDescriptionPopup.js';

const KitCard = ({kitId, renderContent}) => {
  const [data, setData] = useState([]);
  const [openModalId, setOpenModalId] = useState(null); 
  const change_page = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/posts/');
        setData(response.data);
        console.log("requisição do kit card", response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleStartClick = (id) => { 
    setOpenModalId(id); 
  };

  const closeModal = () => {
    setOpenModalId(null); 
  };

  return (
    <div className='kit-cards'>     
          <h2 className='kits-title'>Kits</h2>
        <div className='kit-card-area'>
        {Array.isArray(data) ? (
          data.map(item => (
            <div className='kit-card-item' key={item.ID}>
              <h3 className='kit-card-title'>Kit {item.ID}</h3>
              <div className='kit-card-img-area'>
                <img src={kitImage} alt="" className='kit-card-img'/>
              </div>
              <div className='kit-card-buttons-area'>
                <button type="button" onClick={() => handleStartClick(item.ID)}>Start</button>
              </div>
              {openModalId === item.ID && ( 
                <Modal showModal={openModalId !== null} closeModal={closeModal} kitId={item.ID}  renderContent={renderContent} />
              )}

            </div>
          ))
        ) : (
          <p>Data is not an array.</p>
        )}
        </div>
    </div>
  );
};

export default KitCard;
