import React from 'react';
import './App.css';
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Products from "./admin/Products";
import {BrowserRouter, Route} from "react-router-dom";
import Main from "./main/Main";

function App() {
  return (
    <div className="App">
        <Nav />


            <div className="container-fluid">
                  <div className="row">

                    <Menu />

                    <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">

                        <BrowserRouter>
                            <Route path='/' component={Main} />
                            <Route path='/admin/products' component={Products}/>
                        </BrowserRouter>

                    </main>
                  </div>
            </div>

    </div>
  );
}

export default App;
