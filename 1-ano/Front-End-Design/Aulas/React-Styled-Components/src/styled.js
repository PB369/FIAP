import styled from 'styled-components'

export const DivComponente1 = styled.div`
    background-color: lightgoldenrodyellow;
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

export const Button = styled.button`
    background-color: ${(props) => props.$isOn ? "#00ff00" : "#ffff00"};
    border-radius: 10px;
    padding: 5px;
    color: black;
    border: 1px solid black;
`