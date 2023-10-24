import './App.css'

function App() {
  return (
    <>
      <h1>Aula de Bootstrap</h1>
      <div className="row">
        <div className="col--md-6 col-lg-4 col-xl-3">COL-3</div>
        <div className="col--md-6 col-lg-4 col-xl-3">COL-3</div>
        <div className="col--md-6 col-lg-4 col-xl-3">COL-3</div>
        <div className="col--md-6 col-lg-4 col-xl-3">COL-3</div>
      </div>

      <div className="m-5 bg-dark text-primary text-center container-fluid border">Container</div>
      <div className="text-secondary text-center container-sm border">Container</div>
      <div className="text-sucess text-center container-md border">Container</div>
      <div className="text-danger text-center container-lg border">Container</div>
      <div className="text-primary text-center container-xl border">Container</div>
      <div className="text-primary text-center container-xxl border"><p className='mt-5 me-2 border border-primary'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus, consectetur? Quasi iusto aliquam vero, adipisci hic officia natus vitae eos.</p></div>

      <div className='botoes'>
        <button className='btn btn-outline-primary'>Clique Aqui</button>
        <button className='btn btn-outline-secondary'>Clique Aqui</button>
        <button className='btn btn-outline-success'>Clique Aqui</button>
        <button className='btn btn-outline-danger'>Clique Aqui</button>
        <button className='btn btn-outline-warning'>Clique Aqui</button>
        <button className='btn btn-outline-info'>Clique Aqui</button>
        <button className='btn btn-outline-light'>Clique Aqui</button>
        <button className='btn btn-outline-dark'>Clique Aqui</button>
        <button className='btn btn-outline-link'>Clique Aqui</button>
      </div>

      <table className='mt-4 table table-striped table-bordered border-dark table-hover'>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Endereço</th>
            <th>Telefone</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Bianca</td>
            <td>Rua Tal, 55</td>
            <td>+12 34567-8910</td>
          </tr>
          <tr>
            <td>Bianca</td>
            <td>Rua Tal, 55</td>
            <td>+12 34567-8910</td>
          </tr>
          <tr>
            <td>Bianca</td>
            <td>Rua Tal, 55</td>
            <td>+12 34567-8910</td>
          </tr>
        </tbody>
      </table>
    </>
  )
}

export default App
