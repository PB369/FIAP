import './css/Novidades.scss'
import Carousel from 'react-bootstrap/Carousel';

const Novidades = () => {

  const listItems = [
    {
      name: "boneco1",
      path: "../../../imagens-carrossel/boneco1.jpg",
      lorem: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eum mollitia veniam assumenda fugit quis maiores?"
    },
    {
      name: "boneco2",
      path: "../../../imagens-carrossel/boneco2.png",
      lorem: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo cumque praesentium reiciendis aliquid mollitia."
    },
    {
      name: "chaveiro1",
      path: "../../../imagens-carrossel/chaveiros1.png",
      lorem: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Obcaecati corrupti nam, odit autem laborum sit."
    },
    {
      name: "chaveiro2",
      path: "../../../imagens-carrossel/chaveiros2.png",
      lorem: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum amet tempora praesentium non vel."
    },
    {
      name: "revista1",
      path: "../../../imagens-carrossel/revistas1.jpg",
      lorem: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Amet non quidem atque rerum natus beatae."
    },
    {
      name: "revista2",
      path: "../../../imagens-carrossel/revistas2.jfif",
      lorem: "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aperiam delectus consequatur deleniti molestiae quae?"
    },
    {
      name: "roupa1",
      path: "../../../imagens-carrossel/roupas1.png",
      lorem: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni corrupti ab tenetur assumenda placeat libero."
    },
    {
      name: "roupa2",
      path: "../../../imagens-carrossel/roupas2.png",
      lorem: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eum mollitia veniam assumenda fugit quis maiores?"
    }
  ]

  const carouselItems = listItems.map(item =>
      <Carousel.Item key={item.name} className='item'>
          <img
            className='d-block w-100'
            src={item.path}
            alt={item.name}
            draggable="false"
          />
          <div className='caption d-flex flex-column justify-content-around align-items-center py-3 px-3'>
            <p className='mt-2 text-center'>{item.lorem}</p>
            <button>Ver mais</button>
          </div>
        </Carousel.Item>
    )

  return (
    <section className='d-flex w-10 justify-content-center align-items-center my-5 px-5'>
       <Carousel className='carouselDiv d-flex justify-content-center align-items-center flex-column' data-bs-theme="dark" indicators={false} touch={true} interval={null}>
        {carouselItems}
      </Carousel>
    </section>
  )
}

export default Novidades