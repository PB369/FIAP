import styled from 'styled-components'

const DivComponente2 = styled.div`
    background-color: lightgreen;
    border: 2px solid black;

    h2 {
        text-align: center;
        color: black;
    }

    p {
        text-align: center;
        color: black;
    }
`

export default function Componente2(){
    return(
        <DivComponente2>
            <h2>Componente 2</h2>
            <p>Este é o componente 2</p>
        </DivComponente2>
    )
}