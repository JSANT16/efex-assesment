import { useState } from "react";

type Corrections = {
    [key: string]: string;
}



interface AutocorrectTextareaProps {
    corrections: Corrections;
}

const AutocorrectTextarea: React.FC<AutocorrectTextareaProps> = ({ corrections }) => {
    const [text, setText] = useState('');
    const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setText(event.target.value);
    };

    const handleKeyUp = (event: React.KeyboardEvent<HTMLTextAreaElement>) => {
        if (event.key === ' ') {
            const words = text.trim().split(' ');

            if (words.length > 0) {
                const lastWord = words[words.length - 1];
                const correctedWord = corrections[lastWord as unknown as number] || lastWord;

                words[words.length - 1] = correctedWord;
                setText(words.join(' ') + ' ');
            }
        }
    };
    return (
        <textarea
            value={text}
            onChange={handleChange}
            onKeyUp={handleKeyUp}
            data-testid="textarea"
        />
    )
}

export default AutocorrectTextarea