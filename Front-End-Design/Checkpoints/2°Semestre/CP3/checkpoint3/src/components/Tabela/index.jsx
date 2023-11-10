import './css/Tabela.scss'
import Table from 'react-bootstrap/Table';

const Tabela = () => {
  return (
    <section className='d-flex justify-content-center align-items-center flex-column'>
      <h3 className='text-white mb-4 px-3 text-center'>Confira as nossas promoções!</h3>
      <Table bordered className='table mb-5' style={{width: "50%"}}>
        <thead>
          <tr>
            <th>Categoria</th>
            <th>Produto</th>
            <th>Promoção</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Roupa</td>
            <td className='product'>Camiseta do Venom</td>
            <td>De R$55,00 para R$36,00</td>
          </tr>
          <tr>
            <td>Miniatura</td>
            <td className='product'>Miniatura do Hulk</td>
            <td>De R$102,00 para R$84,50</td>
          </tr>
          <tr>
            <td>Chaveiros</td>
            <td className='product'>Chaveiro do Batman</td>
            <td>De R$7,00 para R$3,80</td>
          </tr>
          <tr>
            <td>Adesivo</td>
            <td className='product'>Pacote de 20 adesivos da DC COMICS</td>
            <td>De R$32,00 para R$24,00</td>
          </tr>
          <tr>
            <td>Revista</td>
            <td className='product'>Revista do Dragon Ball Z</td>
            <td>De R$31,00 para R$27,00</td>
          </tr>
        </tbody>
      </Table>
    </section>
  )
}

export default Tabela