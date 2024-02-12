import { TeamCreationDataPreValidation } from './types'

/**
 * Validation function for first player
 */
export function validateFirstPlayer(
  value: string,
  values: TeamCreationDataPreValidation,
) {
  // if first player value is not set
  if (value === undefined) {
    return 'First player is required'
  }
  // if selected same first and second player
  if (values.secondPlayer && value === values.secondPlayer) {
    return 'First and second player cannot be the same'
  }
  return null
}

export function validateSecondPlayer(
  value: string,
  values: TeamCreationDataPreValidation,
) {
  // if selected same first and second player
  if (values.firstPlayer && value === values.firstPlayer) {
    return 'First and second player cannot be the same'
  }
  return null
}
