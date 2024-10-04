import AutocorrectTextarea from "./components/AutocorrectTextarea"



export const App = () => {
  const corrections = {
    'realy': 'really',
    'wierd': 'weird',
  };
  return (
    <><AutocorrectTextarea corrections={corrections} /></>
  )
}

