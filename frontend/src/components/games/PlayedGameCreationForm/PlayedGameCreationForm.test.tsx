import '@testing-library/jest-dom'

import { render, screen, fireEvent } from '@testing-library/react'
import axios from 'axios'
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

  test('submits form data when submitted', async () => {
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

    jest.mock('axios')
    const mAxiosPost = jest.mocked(axios.post)

    mAxiosPost.mockResolvedValueOnce({ status: 200 })

    // Fill out the form
    fireEvent.change(screen.getByTestId('first-team-goals-input'), {
      target: { value: '3' },
    })
    fireEvent.change(screen.getByTestId('second-team-goals-input'), {
      target: { value: '2' },
    })

    // Submit the form
    fireEvent.click(screen.getByTestId('create-game-button'))

    // Check if the axios post call was made
    expect(mAxiosPost).toHaveBeenCalledWith('http://localhost:8000/games', {
      first_team_id: 1,
      second_team_id: 2,
      first_team_goals: 3,
      second_team_goals: 2,
    })

    // Check if the form is reset after submission
    expect(screen.queryByTestId('first-team-goals-input')).toHaveValue(0)
    expect(screen.queryByTestId('second-team-goals-input')).toHaveValue(0)
  })
})
