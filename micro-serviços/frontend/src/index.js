import React from 'react';
import ReactDOM from 'react-dom';
import Helmet from 'react-helmet';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.min.css';

import ListTarefa  from './templates/list_tarefas';
import Tarefa from './templates/tarefa';
import './style.css'

ReactDOM.render(
    <div>
        <Helmet>
            <html lang="pt-br" />
            <title>Tarefas</title>
            <meta name="description" content="Sistema de gestão de Tarefas" />
            <meta name="theme-color" content="#FF0000" />
            <meta http-equiv="Content-Language" content="pt-br" />
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        </Helmet>
        <BrowserRouter>
            <Routes>
                <Route path="/">
                <Route index element={<ListTarefa />} />
                <Route path="tarefa/" >
                    <Route index element={<Tarefa />} />
                    <Route  path=":id" element={<Tarefa />} />
                </Route>
                </Route>
            </Routes>
        </BrowserRouter>
    </div>,
    document.getElementById('root')
);