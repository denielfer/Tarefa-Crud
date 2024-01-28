import React from 'react'
import 'bootstrap'
import './style.css'
import Accordion from '../../components/accordion/accordion'
import { BACKEND_URL } from '../../config/config'

class ListTarefa extends React.Component{
    minhaRef = React.createRef();
    constructor(props){
        super(props);

        this.state = {
            tarefas : [
            ]
        }
    }

    componentDidMount(){
        fetch(BACKEND_URL+"tarefa/")
        .then(resposta=> resposta.json())
        .then(dados => this.setState(dados))
        .catch(error => {this.setState({tarefas:null})})
    }

    hidden_all = () =>{
        this.state.tarefas.map(
            (_tarefa) =>{
                document.getElementById(_tarefa.id).hidden = true
                return 1;
            }
        )
    }

    show_only = (id)=>{
        this.hidden_all();
        document.getElementById(id).hidden = false;
        document.getElementById(id).setAttribute('overflow','visible') ;
        console.log(document.getElementById(id));
    }
    

    deletartarefa = (id)=>{
        fetch("http://localhost:8000/tarefa/"+id, {method:'DELETE'})
        .then(resposta=> 
            {
                if(resposta.ok){
                    window.location.reload();
                }else{
                    console.log(resposta.json())
                    alert("Não foi possivel deletar tarefa");
                }
            })
        .then(dados => this.setState(dados))
        .catch(error => {this.setState({tarefas:[]})})

    }

    redirecionar_editar_tarefa = (id)=>{
        window.location.href = "/tarefa/"+id
    }

    render_table = () =>{
        return (
            <div style={{color: 'rgba(255, 255, 255, 0.633)'}}>
                <h1>Lista de Tarefas  
                    <br></br>
                    <h6>Quantidade de itens: {this.state.tarefas.length}</h6>
                    <button class="btn btn-success" onClick={() => { this.redirecionar_editar_tarefa('') }} >Adicionar Item</button>
                </h1>
                <Accordion >
                        {this.state.tarefas.map((tarefa) =>(
                            <div
                                label={tarefa.titulo+ ', para: '+tarefa.data.split('-').reverse().join('-')+', estado: '+tarefa.status}
                                
                                >
                                <h5>Comentario: </h5>
                                <p>
                                                    {tarefa.descricao}
                                </p>
                                <button class="btn btn-info" onClick={() => { this.redirecionar_editar_tarefa(tarefa.id) }} style={{margin:'5px'}} >Editar</button>
                                <button class="btn btn-danger" onClick={() => { this.deletartarefa(tarefa.id)}} style={{margin:'5px'}}> Deletar </button>
                            </div>))
                        }
                </Accordion>
            </div>
        );
    }

    // problemas ao conseguir dados do banco 
    render_problemas = () =>{
        return (
            <div style={{color: 'rgba(255, 255, 255, 0.633)'}}>
                <h2>
                    Não foi possivel conectar com o backend, entre em contanto com suporte
                </h2>
            </div>
        )
    }

    render(){
        if (this.state.tarefas === null){
            return this.render_problemas()
        }
        return this.render_table()
    }

}

export default ListTarefa