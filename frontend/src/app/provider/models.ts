export interface Questionnaire {
    questions: [
        {
            question: string,
            options: string
        }
    ];
}

export interface QuestionnaireAnswers {
    name: string;
    answers: string[];
}

export interface Stage {
    story: string[];
    destinationCoords?: number[];
    destinationName?: string;
    challenge?: Challenge;
}

export interface Challenge {
    challenge: string;
    challenge_type: number;
    options?: string[];
    right_answer: string | number[] | string[];
}

export interface ChallengeOutcome {
    challengeOutcome: boolean;
    playerLocation?: number[];
}
