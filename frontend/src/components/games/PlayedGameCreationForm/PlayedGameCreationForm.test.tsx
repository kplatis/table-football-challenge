import '@testing-library/jest-dom'

import { render, screen } from '@testing-library/react'
import PlayedGameCreationForm from '../PlayedGameCreationForm'
import { mockTeams } from '@/__tests__/mockData/teams'
import Providers from '@/components/Providers'
// Mock axios post
jest.mock('axios')

describe('PlayedGameCreationForm', () => {
  test('renders loader when teams are loading', () => {
    render(
      <Providers>
        <PlayedGameCreationForm />
      </Providers>,
    )
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders form when teams are loaded', () => {
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockTeams,
      }))

    render(
      <Providers>
        <PlayedGameCreationForm />
      </Providers>,
    )

    // Check if form elements are rendered
    expect(screen.queryByTestId('first-team-select')).toBeInTheDocument()
    expect(screen.queryByTestId('second-team-select')).toBeInTheDocument()
    expect(screen.queryByTestId('first-team-goals-input')).toBeInTheDocument()
    expect(screen.queryByTestId('second-team-goals-input')).toBeInTheDocument()
    expect(screen.queryByTestId('create-game-button')).toBeInTheDocument()
  })
})
