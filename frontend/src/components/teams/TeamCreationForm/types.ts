export type TeamCreationDataPreValidation = {
  name: string
  firstPlayer: string | null
  secondPlayer: string | null
}

export type TeamCreationDataPostValidation = {
    name: string
    firstPlayer: string
    secondPlayer: string | null
  }