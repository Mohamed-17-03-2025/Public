import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import Lottie from "lottie-react";
import Animation from "./assets/Animation.json";
import axios from 'axios';

function App() 
{
  const ai_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=API_KEY)"

  const [suggestions, setSuggetion] = useState(["What is React.js ?", "What is JavaScript ?", "How to build an AI chatbot ?"]);

  const [message,setmessage] = useState([]);
  
  const [input, setInput] = useState("");



  const handleSubmit = async () => 
  {
    let usermessage = {sender:"user",text:input};
    setmessage(prev =>[...prev,usermessage]);

    try
    {
     const response = await axios.post(ai_url,
                                      {
                                        contents:[{
                                        parts:   [{"text": input}]
                                                }]
                                      }
                                      )
     if(response.data)
     { 
        let aimessage = {sender: "AI", text: response.data.candidates[0].content.parts[0].text};
        setmessage(prev => [...prev, aimessage]);
     }                                    
    }

    catch(error)
    {
        let errormessage = {sender: "AI", text: "Sorry, I am not able to answer this question."};
        setmessage(prev => [...prev, errormessage]);
    }

    setInput("");
  }

  return (
          <div className='vh-100'>
            <div className=' h-100'>
              <div className='card border-0 shadow-sm bg-transparent h-100'>
                <div className='card-body chatbot-body'>

                  <div className='d-flex justify-content-center align-items-center'>
                    <div className='my-4'>
                      <Lottie animationData={Animation} style={{width: "10rem"}} />
                    </div>
                  </div>


                  <div className='row row-cols-4'>
                    {
                      suggestions.map(
                                    (currEle, Index)=>{return(<div className='col'>
                                                                <div className='card border-0 shadow-sm suggestion-card h-100'>
                                                                  <div className='card-body d-flex justify-content-center align-items-center'>  
                                                                    {/* <h5 className='card-title'>React JS</h5> */}
                                                                    <p className='card-text'>{currEle}</p>
                                                                  </div>
                                                                </div>
                                                              </div>
                                                              )
                                                      }
                                      )
                    }
                  </div> 
                  {
                    message.length > 0 ?
                    <>
                      {
                        message.map(
                                    (currEle, index) => {return(<div className={currEle.sender === "user" ? 'd-flex justify-content-end w-100' : 'd-flex justify-content-start w-100' }>
                                                                  <div className={`${currEle.sender}-response-messages`}>
                                                                    <p className='mb-0'>{currEle.text}</p>
                                                                  </div>
                                                                </div>  
                                                               )
                                                        }
                                   )
                      }
                    </> : null
                  }
                  <div>
                    
                  </div>

                </div>
                <div className='card-footer'>
                  <div className='input-group'>
                    <input type='text' className='form-control' value={input} placeholder='Ask me anything...' onChange={(e)=>setInput(e.target.value)}/>
                    <button className='btn btn-primary' onClick={handleSubmit}>Send</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
         )
}

export default App
