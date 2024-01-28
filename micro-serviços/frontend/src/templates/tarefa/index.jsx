import React from 'react'
import 'bootstrap'
import { useFormik } from "formik";
import * as Yup from "yup";
import { motion as m } from "framer-motion";
import { BACKEND_URL } from '../../config/config'
import axios from 'axios';
import { useParams } from 'react-router-dom';


export default function Tarefa(){
  const { id } = useParams() 
  const [dados, setDados] = React.useState({titulo:"",descricao:"",data:'',status:'Pendente'});
  const formik = useFormik({
    initialValues: dados,
    validationSchema: Yup.object({
      titulo: Yup.string()
        .max(50, "Titulo precisa ser até 50 caracteres")
        .required("Titulo é obrigatorio"),
        data: Yup.date()
        .required("Uma data é requerida"),
    }),

    onSubmit: (values) => {
      values.status = values.status.toLowerCase().charAt(0)
      if(id){
        axios.put(BACKEND_URL+'tarefa/'+id, values,{
            headers: {
              'Content-Type':'application/json'
            }})
        .then(data => {
          window.location.href = "/"
        })
        .catch(error => {
          try{
            console.log(error.response)
            alert(error.response.data.error)
          } catch(err){
            alert('Verifique a conecção com a internet se o problema persistir, entre em contato com o suporte.')
          }
        })
      }else{
        axios.post(BACKEND_URL+'tarefa/', values,{
          headers: {
            'Content-Type':'application/json'
          }})
      .then(data => {
        window.location.href = "/"
      })
      .catch(error => {
        try{
          console.log(error.response)
          alert(error.response.data.error)
        } catch(err){
          alert('Verifique a conecção com a internet se o problema persistir, entre em contato com o suporte.')
        }
      })
      }
    },
    enableReinitialize:true,
  });
  
 React.useEffect(() => {
  const find_tarefa = (id) => {
    try{
      axios.get(BACKEND_URL+'tarefa/'+id)
      .then(response =>{
        formik.values = response.data
        setDados(response.data)
        console.log(formik.values)
      }).catch(error =>{
        alert(error.response.data.error+'\n Redirecionando a pagina inicial, se o erro percisiste contacte o suporte.')
        window.location.reload()
      })
    }catch{
      alert('Não foi possivel acessar dados, espere alguns instantes e tente novamente\nSe o problema persisti entre em contato com o suporte.')
      window.location.href = "/"
    }
  };
  if(id){
    console.log('buscando dados')
    find_tarefa(id);
  }
  }, []);
  return (
    <m.div style={{color: 'rgba(255, 255, 255, 0.7)'}}
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    exit={{ opacity: 0 }}
    className="absolute w-full"
    >
      <main style={{display: 'flex',justifyContent: 'center'}}>
        <form
          onSubmit={formik.handleSubmit}
          className="flex rounded font-latoRegular"
        >
          <div>
            <h1>
              Criar nova tarefa
            </h1>
            <div className="mt-6 ">
              <div className="pb-4">
                <label style={{color:formik.touched.titulo && formik.errors.titulo? "red":''}}
                  htmlFor="titulo"
                >
                  {formik.touched.titulo && formik.errors.titulo
                    ? formik.errors.titulo
                    : "Titulo"}
                </label>
                <br></br>
                <input
                  className="border-2 p-1 rounded  "
                  type="text"
                  name="titulo"
                  placeholder="Difite o titulo da tarefa"
                  onChange={formik.handleChange}
                  value={formik.values.titulo}
                  onBlur={formik.handleBlur}
                />
              </div>
              
              <div className="pb-4">
                <label style={{color:formik.touched.data && formik.errors.data? "red":''}}
                  htmlFor="data"
                >
                  {formik.touched.data && formik.errors.data
                    ? formik.errors.data
                    : "Data"}
                </label>
                <br></br>
                <input
                  className="border-2 border-gray-500 p-2 rounded w-1/2 focus:border-teal-500 focus:ring-teal-500 "
                  type="date"
                  name="data"
                  onChange={formik.handleChange}
                  value={formik.values.data}
                  onBlur={formik.handleBlur}
                />
              </div>

              <div className="pb-4">
                <label
                  htmlFor="status"
                  className="block font-latoBold text-sm pb-2"
                >
                  Estado: 
                </label>
                <select
                  className="border-2 border-gray-500 p-1 rounded w-1/2 focus:border-teal-500 focus:ring-teal-500"
                  name="status"
                  onChange={formik.handleChange}
                  value={formik.values.status}
                >
                  <option value='p'>Pendente</option>
                  <option value='e'>Executando</option>
                  <option value='c'>Concluída</option>
                </select>
              </div>
              
              <div className="pb-4">
                <label
                  htmlFor="descricao"
                >
                  Descrição
                </label>
                <br></br>
                <textarea style={{ textAlign: 'center' , width: '50vw', maxWidth:'90vw', minHeight:'10vh'}}
                  // cols={100}
                  className="border-2 border-gray-500 rounded w-1 focus:border-teal-500 focus:ring-teal-500 "
                  type="text"
                  name="descricao"
                  onChange={formik.handleChange}
                  value={formik.values.descricao}
                  onBlur={formik.handleBlur}
                />
              </div>

              <button
                type="submit"
                style={{ backgroundColor: typeof(id) == "undefined" && (formik.errors.titulo || formik.errors.data || (!formik.touched.data || !formik.touched.titulo))? 'red':'green'}}
                className="p-3 mt-6 rounded w-full"
              >
                Enviar
              </button>
            </div>
          </div>
        </form>
      </main>
    </m.div>)
};