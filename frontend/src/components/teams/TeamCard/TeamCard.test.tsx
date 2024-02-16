import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import TeamCard from '../TeamCard'
import { mockPlayers } from '@/__tests__/mockData/players'
import Providers from '@/components/Providers'

// Mock useRouter hook
jest.mock('next/navigation')

describe('TeamCard', () => {
  test('renders team name and players correctly', () => {
    render(
      <Providers>
        <TeamCard
          id={1}
          name="team1"
          firstPlayer={mockPlayers[0]}
          secondPlayer={mockPlayers[1]}
        />
      </Providers>,
    )

    // Check if team name is rendered
    expect(screen.getByText('team1')).toBeInTheDocument()

    // Check if player names are rendered
    expect(screen.getByText('Player1')).toBeInTheDocument()
    expect(screen.getByText('Player2')).toBeInTheDocument()
  })
})
