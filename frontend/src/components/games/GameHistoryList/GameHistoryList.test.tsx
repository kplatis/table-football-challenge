import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import GameHistoryList from '.'
import { mockGames } from '@/__tests__/mockData/games'
import { mockTeams } from '@/__tests__/mockData/teams'
import Providers from '@/components/Providers'

describe('GameHistoryList Component', () => {
  const mockData = mockGames

  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('renders game history correctly when data is loaded', () => {
    const mockUseGames = jest.fn(() => ({ isLoading: false, data: mockData }))
    require('@/hooks/useGames').default = mockUseGames

    render(
      <Providers>
        <GameHistoryList firstTeam={mockTeams[0]} secondTeam={mockTeams[1]} />
      </Providers>,
    )

    expect(screen.getByText('2 - 1')).toBeInTheDocument()
    expect(screen.getByText('6 - 0')).toBeInTheDocument()
  })

  it('does not render anything when no data is available', () => {
    const mockUseGames = jest.fn(() => ({ isLoading: false, data: null }))
    require('@/hooks/useGames').default = mockUseGames

    render(
      <Providers>
        <GameHistoryList firstTeam={mockTeams[0]} secondTeam={mockTeams[1]} />
      </Providers>,
    )
    expect(screen.queryByTestId('loader')).not.toBeInTheDocument()
    expect(screen.queryByText('2 - 1')).not.toBeInTheDocument()
    expect(screen.queryByText('6 - 0')).not.toBeInTheDocument()
  })
})
