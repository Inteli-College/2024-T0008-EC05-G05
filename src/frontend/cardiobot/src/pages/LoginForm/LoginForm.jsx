import React, {useState} from 'react';
import { useNavigate } from "react-router-dom";
import './LoginForm.css';
import { FaUser, FaLock } from "react-icons/fa";

const LoginForm = () => {

    const change_page = useNavigate();


    // Variavel de estado para armazenar o valor de email e senha
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // Função que checa se o email e senha estão corretos 
    const handleSignIn = (e) => {
        e.preventDefault();

        if (email === 'admin' && password === 'admin') {
            console.log("Login com sucesso")
            change_page("/dashboard");

        } else {
            alert('Email ou senha incorretos');
        }
    };

    return (
        <div className='master'>
            <div className='wrapper'>
                <from onSubmit={handleSignIn} action="">
                    <h1>Login</h1>

                    <div className='input-box'>
                        <input type='text' 
                        placeholder='Usuário' required              
                        value={email}                             
                        onChange={(e) => setEmail(e.target.value)} 
                         />
                        <FaUser className='icon' />
                    </div>

                    <div className='input-box'>
                        <input 
                        type='password' 
                        placeholder='Senha' required 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                        />
                        <FaLock className='icon' />
                    </div>

                    <div className='remember-forgot'>
                        <label>
                            <input type='checkbox' />lembrar de mim
                        </label>
                    </div>
                    <div>
                        <button type='submit' onClick={handleSignIn}>Login</button>
                    </div>


                </from>
            </div>
        </div>
    )
}

export default LoginForm;