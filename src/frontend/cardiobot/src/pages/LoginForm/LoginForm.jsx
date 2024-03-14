import React from 'react';
import './LoginForm.css';
import { FaUser, FaLock } from "react-icons/fa";

const LoginForm = () => {
    return (
        <div className='master'>
            <div className='logo'>
                <h2>Cardio-Bot</h2>
            </div>
            <main className='container'>
                <div className='wrapper'>
                    <from action="">
                        <h1>Login</h1>

                        <div className='input-box'>
                            <input type='text' placeholder='Usuário' required />
                            <FaUser className='icon' />
                        </div>

                        <div className='input-box'>
                            <input type='password' placeholder='Senha' required />
                            <FaLock className='icon' />
                        </div>

                        <div className='remember-forgot'>
                            <label>
                                <input type='checkbox' />lembrar de mim
                            </label>
                        </div>
                        <div>
                            <button type='submit'>Login</button>
                        </div>
                    </from>
                </div>
            </main>
        </div>
    )
}

export default LoginForm;