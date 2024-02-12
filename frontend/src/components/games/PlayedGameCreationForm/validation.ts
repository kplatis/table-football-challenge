import { GameCreationDataPreValidation } from './types'

/**
 * Validation function for first player
 */
export function validateFirstTeam(
  value: number,
  values: GameCreationDataPreValidation,
) {
  // if first player value is not set
  if (value === null) {
    return 'First Team is required'
  }
  // if selected same first and second player
  if (values.secondTeamId && value === values.secondTeamId) {
    return 'First and second team cannot be the same'
  }
  return null
}

/**
 * Validation function for first player
 */
export function validateSecondTeam(
  value: number,
  values: GameCreationDataPreValidation,
) {
  // if first player value is not set
  if (value === null) {
    return 'Second Team is required'
  }
  // if selected same first and second player
  if (values.firstTeamId && value === values.firstTeamId) {
    return 'First and second team cannot be the same'
  }
  return null
}
