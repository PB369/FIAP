import './css/Categorias.scss'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

const Categorias = () => {

  const listCards = [
    {
      name: "Bonecos",
      path: "../../../imagens-categorias/bonecos.jpg"
    },
    {
      name: "Chaveiros",
      path: "../../../imagens-categorias/chaveiros.png"
     },
    {
      name: "Revistas",
      path: "../../../imagens-categorias/revistas.jpg"
     },
     {
      name: "Roupas",
      path: "../../../imagens-categorias/roupas.png"
     },
    {
      name: "Adesivos",
      path: "../../../imagens-categorias/adesivos.jfif"
     },
    {
      name: "Miniaturas",
      path: "../../../imagens-categorias/miniaturas.jfif"
     }
  ]

  const cards = listCards.map(card =>
    <Card style={{ width: '18rem' }} key={card.name} className='cardItem mx-4 my-4'>
      <Card.Img variant="top" src={card.path} className='py-2 px-2'/>
      <Card.Body className='cardBody d-flex justify-content-center align-items-center flex-column'>
        <Card.Title className='cardTitle mb-4'>{card.name}</Card.Title>
        <Button variant="primary" className='cardButton mb-2'>Acessar</Button>
      </Card.Body>
    </Card>
  )

  return (
    <section className='my-5 categories d-flex justify-content-center align-items-center'>
      <div className="cardDiv d-flex justify-content-center align-items-center flex-row row w-100 container">
        {cards}
      </div>
    </section>
  )
}

export default Categorias