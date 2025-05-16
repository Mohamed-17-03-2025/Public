import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import Lottie from "lottie-react";
import Animation from "./assets/Animation.json";

function App() 
{
  const [suggestions, setSuggetion] = useState(["What is React.js ?", "What is JavaScript ?", "How to build an AI chatbot ?"])

  return (
          <>
          <div className='container'>

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
            
          </div>
          </>
         )
}

export default App
