import '@testing-library/jest-dom'

import { render, screen } from '@testing-library/react'
import PlayLiveGame from '../PlayLiveGame'
import Providers from '@/components/Providers'
import { mockTeams } from '@/__tests__/mockData/teams'

// Mock axios post
jest.mock('axios')

describe('PlayLiveGame', () => {
  test('renders loader when teams are loading', () => {
    render(
      <Providers>
        <PlayLiveGame />
      </Providers>,
    )
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders team selection form when teams are loaded', () => {
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockTeams,
      }))

    render(
      <Providers>
        <PlayLiveGame />
      </Providers>,
    )

    // Check if team selection form is rendered
    expect(screen.queryByText('Start the Game!')).toBeInTheDocument()
  })
})
