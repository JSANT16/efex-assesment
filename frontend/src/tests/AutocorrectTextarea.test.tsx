import { render, fireEvent } from '@testing-library/react'
import AutocorrectTextarea from '../components/AutocorrectTextarea'


describe('AutocorrectTextarea', () => {
    const corrections = {
        'realy': 'really',
        'weird': 'weird',
    }


    test('updates text state on change', () => {
        const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />)
        const textarea = getByTestId('textarea') as HTMLTextAreaElement

        fireEvent.change(textarea, { target: { value: 'Hello' } })
        expect(textarea.value).toBe('Hello')
    })

    test('autocorrects word on space key press', () => {
        const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />)
        const textarea = getByTestId('textarea') as HTMLTextAreaElement

        fireEvent.change(textarea, { target: { value: 'This is a realy' } })
        fireEvent.keyUp(textarea, { key: ' ' })

        expect(textarea.value).toBe('This is a really ')
    })

    test('does not autocorrect if the word is not in corrections', () => {
        const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />)
        const textarea = getByTestId('textarea') as HTMLTextAreaElement

        fireEvent.change(textarea, { target: { value: 'This is strange' } })
        fireEvent.keyUp(textarea, { key: ' ' })

        expect(textarea.value).toBe('This is strange ')
    })

    test('correctly handles multiple spaces and words', () => {
        const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />)
        const textarea = getByTestId('textarea') as HTMLTextAreaElement

        fireEvent.change(textarea, { target: { value: 'That is a realy' } })
        fireEvent.keyUp(textarea, { key: ' ' })

        expect(textarea.value).toBe('That is a really ')
    })
})
